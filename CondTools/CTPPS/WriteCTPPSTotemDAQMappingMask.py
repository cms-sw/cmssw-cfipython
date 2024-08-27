import FWCore.ParameterSet.Config as cms

def WriteCTPPSTotemDAQMappingMask(**kwargs):
  mod = cms.EDAnalyzer('WriteCTPPSTotemDAQMappingMask',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
