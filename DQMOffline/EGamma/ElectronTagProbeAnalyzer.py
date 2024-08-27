import FWCore.ParameterSet.Config as cms

def ElectronTagProbeAnalyzer(**kwargs):
  mod = cms.EDProducer('ElectronTagProbeAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
