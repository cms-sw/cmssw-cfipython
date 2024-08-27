import FWCore.ParameterSet.Config as cms

def ElectronAnalyzer(**kwargs):
  mod = cms.EDProducer('ElectronAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
