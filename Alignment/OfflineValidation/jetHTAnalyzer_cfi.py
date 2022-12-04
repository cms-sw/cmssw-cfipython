import FWCore.ParameterSet.Config as cms

jetHTAnalyzer = cms.EDAnalyzer('JetHTAnalyzer',
  vtxCollection = cms.InputTag('offlinePrimaryVerticesFromRefittedTrks'),
  triggerResults = cms.InputTag('TriggerResults', '', 'HLT'),
  trackCollection = cms.InputTag('TrackRefitter'),
  printTriggerTable = cms.int32(0),
  minVertexNdf = cms.double(10),
  minVertexMeanWeight = cms.double(0.5),
  profilePtBorders = cms.vdouble(
    3,
    5,
    10,
    20,
    50,
    100
  ),
  iovList = cms.vdouble(
    0,
    500000
  ),
  mightGet = cms.optional.untracked.vstring
)
