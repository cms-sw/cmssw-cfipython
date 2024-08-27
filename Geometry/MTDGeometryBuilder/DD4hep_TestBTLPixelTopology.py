import FWCore.ParameterSet.Config as cms

def DD4hep_TestBTLPixelTopology(**kwargs):
  mod = cms.EDAnalyzer('DD4hep_TestBTLPixelTopology',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
