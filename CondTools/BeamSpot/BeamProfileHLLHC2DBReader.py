import FWCore.ParameterSet.Config as cms

def BeamProfileHLLHC2DBReader(*args, **kwargs):
  mod = cms.EDAnalyzer('BeamProfileHLLHC2DBReader',
    rawFileName = cms.untracked.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
