import FWCore.ParameterSet.Config as cms

def JetHTAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('JetHTAnalyzer',
    vtxCollection = cms.InputTag('offlinePrimaryVerticesFromRefittedTrks'),
    triggerResults = cms.InputTag('TriggerResults', '', 'HLT'),
    trackCollection = cms.InputTag('TrackRefitter'),
    printTriggerTable = cms.untracked.int32(0),
    minVertexNdf = cms.untracked.double(10),
    minVertexMeanWeight = cms.untracked.double(0.5),
    profilePtBorders = cms.untracked.vdouble(
      3,
      5,
      10,
      20,
      50,
      100
    ),
    iovList = cms.untracked.vint32(
      0,
      500000
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
