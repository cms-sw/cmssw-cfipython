import FWCore.ParameterSet.Config as cms

def SiPhase2BadStripChannelReader(**kwargs):
  mod = cms.EDAnalyzer('SiPhase2BadStripChannelReader',
    printVerbose = cms.untracked.bool(False),
    printDebug = cms.untracked.int32(1),
    label = cms.untracked.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
