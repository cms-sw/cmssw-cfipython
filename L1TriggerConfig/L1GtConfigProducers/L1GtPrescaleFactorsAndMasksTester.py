import FWCore.ParameterSet.Config as cms

def L1GtPrescaleFactorsAndMasksTester(**kwargs):
  mod = cms.EDAnalyzer('L1GtPrescaleFactorsAndMasksTester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
