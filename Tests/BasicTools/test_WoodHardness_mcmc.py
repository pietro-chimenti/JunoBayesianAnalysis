#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 08:31:33 2021

@author: P.Chimenti

This code models a bayesian mcmc on the data about wood hardness from table 15.5 of Dekking, et.al, "A Modern Introduction to
    Probability and Statistics" 

"""

import numpy as np
import emcee

class WoodHardness_mcmc:
    """ This class allow to run bayesian MCMC to analisez thw wood hardness data """
    
    """ The wood hardness data: """

    Data = np.array([
            [24.7,484],
            [24.8,427],
            [27.3,413],
            [28.4,517],
            [28.4,549],
            [29.0,648],
            [30.3,587],
            [32.7,704],
            [35.6,979],
            [38.5,914],
            [38.8,1070],
            [39.3,1020],
            [39.4,1210],
            [39.9,989],
            [40.3,1160],
            [40.6,1010],
            [40.7,1100],
            [40.7,1130],
            [42.9,1270],
            [45.8,1180],
            [46.9,1400],
            [48.2,1760],
            [51.5,1710],
            [51.5,2010],
            [53.4,1880],
            [56.0,1980],
            [56.5,1820],
            [57.3,2020],
            [57.6,1980],
            [59.2,2310],
            [59.8,1940],
            [66.0,3260],
            [67.4,2700],
            [68.8,2890],
            [69.1,2740],
            [69.1,3140]])
    Data_x = Data[:,0]
    Data_y = Data[:,1]

    def __init__(self):
        print("Hello WoodHardness_mcmc!")

    def log_likelihood(self, theta):
        """ Likelihood of the model """
        return 0
    
    def log_prior(self, theta):
        """ Model prior """
        return 0
    
    def log_probability(self, theta):
        """ Posterior probability
        for now just gaussian centered in zero and sigma 1 """        
        log_prob = -1.0*(sum(theta**2))/2. 
        result = [log_prob] 
        result.extend(np.ones(self.nblobs))
        return result
        
    def reset(self, nparams = 3, itheta = [], nwalkers = 16, nsamples = 100, nblobs = 1, step_factor = 1.0, move_cov = []):
        """ This function set initial configuration to run the mcmc 
        nparams : number of parameters
        itheta : parameters initial values
        nwalkers : number of walker for ensamble sampling
        nsamples : sample of mcmc
        nblobs : number of blobs (see emcee docs)
        step_factor :  to adjust the step size
        move_cov : covariance of the gaussian move """
        if not any(itheta) :
            self.nparams = nparams
            self.itheta  = np.zeros(nparams)
        else :
            self.nparams = len(itheta)
            self.itheta  = itheta
        self.nwalkers = nwalkers
        if not any(move_cov) :
            self.move_cov   = step_factor*np.ones(self.nparams)
        self.step_factor    = step_factor
        self.nsamples       = nsamples
        self.nblobs         = nblobs
        
    def run_mcmc(self, thin_by = 1):
        """ Here we actually run the MCMC with gaussian moves.
        The function returns parameters samples and blobs 
        
        Thin_by : multiply this number to the number of samples to save to get the total samples
        
        """
        iwalkers = np.array(self.itheta)+self.move_cov*np.random.randn(self.nwalkers,self.nparams)
        print(iwalkers.shape)
        nwalkers, ndim     = iwalkers.shape
        sampler = emcee.EnsembleSampler(
                nwalkers,
                ndim,
                self.log_probability,
                    moves=[
                            (emcee.moves.StretchMove(live_dangerously = True), 0.8),
                            (emcee.moves.GaussianMove(self.move_cov,  mode="sequential"), 0.2)
                            ],
                )
        sampler.run_mcmc(iwalkers, self.nsamples, progress=True, skip_initial_state_check = True, thin_by = thin_by)
        flat_samples = sampler.get_chain(flat=True)
        blobs        = sampler.get_blobs(flat=True)
        return flat_samples, blobs

    

