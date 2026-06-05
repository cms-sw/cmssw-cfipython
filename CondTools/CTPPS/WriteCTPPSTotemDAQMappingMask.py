import FWCore.ParameterSet.Config as cms

def WriteCTPPSTotemDAQMappingMask(*args, **kwargs):
  mod = cms.EDAnalyzer('WriteCTPPSTotemDAQMappingMask',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
