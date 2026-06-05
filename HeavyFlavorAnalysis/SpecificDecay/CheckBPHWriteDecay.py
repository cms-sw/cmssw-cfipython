import FWCore.ParameterSet.Config as cms

def CheckBPHWriteDecay(*args, **kwargs):
  mod = cms.EDAnalyzer('CheckBPHWriteDecay',
    candsLabel = cms.vstring(),
    runNumber = cms.uint32(0),
    evtNumber = cms.uint32(0),
    fileName = cms.untracked.string(''),
    writePtr = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
