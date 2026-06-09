import FWCore.ParameterSet.Config as cms

def BeamProfile2DBReader(*args, **kwargs):
  mod = cms.EDAnalyzer('BeamProfile2DBReader',
    rawFileName = cms.untracked.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
