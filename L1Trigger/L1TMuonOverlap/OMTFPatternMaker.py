import FWCore.ParameterSet.Config as cms

def OMTFPatternMaker(*args, **kwargs):
  mod = cms.EDAnalyzer('OMTFPatternMaker',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
