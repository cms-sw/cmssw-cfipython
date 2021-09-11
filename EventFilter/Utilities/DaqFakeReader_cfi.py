import FWCore.ParameterSet.Config as cms

DaqFakeReader = cms.EDProducer('DaqFakeReader',
  emptyEvents = cms.untracked.bool(False),
  fillRandom = cms.untracked.bool(False),
  meanSize = cms.untracked.uint32(1024),
  width = cms.untracked.uint32(1024),
  injectErrPpm = cms.untracked.uint32(1024),
  tcdsFEDID = cms.untracked.uint32(1024),
  mightGet = cms.optional.untracked.vstring
)
