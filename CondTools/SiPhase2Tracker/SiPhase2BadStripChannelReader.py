import FWCore.ParameterSet.Config as cms

def SiPhase2BadStripChannelReader(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPhase2BadStripChannelReader',
    printVerbose = cms.untracked.bool(False),
    printDebug = cms.untracked.int32(1),
    label = cms.untracked.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
