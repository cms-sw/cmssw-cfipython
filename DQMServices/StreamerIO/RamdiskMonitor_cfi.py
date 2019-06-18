import FWCore.ParameterSet.Config as cms

RamdiskMonitor = cms.EDProducer('RamdiskMonitor',
  streamLabels = cms.required.untracked.vstring,
  runNumber = cms.required.untracked.uint32,
  runInputDir = cms.required.untracked.string,
  mightGet = cms.optional.untracked.vstring
)
