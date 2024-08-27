import FWCore.ParameterSet.Config as cms

def RawDataConverter(**kwargs):
  mod = cms.EDAnalyzer('RawDataConverter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
