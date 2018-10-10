import FWCore.ParameterSet.Config as cms

dtUnpackingModule = cms.EDProducer('DTUnpackingModule',
  dataType = cms.string('DDU'),
  inputLabel = cms.InputTag('rawDataCollector'),
  useStandardFEDid = cms.bool(True),
  minFEDid = cms.untracked.int32(770),
  maxFEDid = cms.untracked.int32(779),
  readOutParameters = cms.PSet(
    debug = cms.untracked.bool(False),
    rosParameters = cms.PSet(
      writeSC = cms.untracked.bool(True),
      readingDDU = cms.untracked.bool(True),
      performDataIntegrityMonitor = cms.untracked.bool(False),
      readDDUIDfromDDU = cms.untracked.bool(True),
      debug = cms.untracked.bool(False),
      localDAQ = cms.untracked.bool(False)
    ),
    performDataIntegrityMonitor = cms.untracked.bool(False),
    localDAQ = cms.untracked.bool(False)
  ),
  dqmOnly = cms.bool(False)
)
