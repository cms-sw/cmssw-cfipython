import FWCore.ParameterSet.Config as cms

def DQMFileSaverPB(*args, **kwargs):
  mod = cms.EDAnalyzer('DQMFileSaverPB',
    fakeFilterUnitMode = cms.untracked.bool(False),
    streamLabel = cms.untracked.string('streamDQMHistograms'),
    tag = cms.untracked.string('UNKNOWN'),
    producer = cms.untracked.string('DQM'),
    referenceHandling = cms.untracked.string('all'),
    referenceRequireStatus = cms.untracked.int32(100),
    path = cms.untracked.string('./'),
    runNumber = cms.untracked.int32(111),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
