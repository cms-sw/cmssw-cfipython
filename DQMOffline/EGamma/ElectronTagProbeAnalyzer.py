import FWCore.ParameterSet.Config as cms

def ElectronTagProbeAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('ElectronTagProbeAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
