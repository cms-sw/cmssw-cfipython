import FWCore.ParameterSet.Config as cms

def V0Monitor(*args, **kwargs):
  mod = cms.EDProducer('V0Monitor',
    FolderName = cms.string('Tracking/V0Monitoring'),
    v0 = cms.InputTag('generalV0Candidates', 'Kshort'),
    beamSpot = cms.InputTag('offlineBeamSpot'),
    primaryVertex = cms.InputTag('offlinePrimaryVertices'),
    lumiScalers = cms.InputTag('scalersRawToDigi'),
    forceSCAL = cms.bool(True),
    metadata = cms.InputTag('onlineMetaDataDigis'),
    pvNDOF = cms.int32(4),
    histoPSet = cms.PSet(
      lumiPSet = cms.PSet(
        nbins = cms.int32(3700),
        xmin = cms.double(0),
        xmax = cms.double(14000)
      ),
      massPSet = cms.PSet(
        nbins = cms.int32(100),
        xmin = cms.double(0.4),
        xmax = cms.double(0.6)
      ),
      ptPSet = cms.PSet(
        nbins = cms.int32(100),
        xmin = cms.double(0),
        xmax = cms.double(50)
      ),
      etaPSet = cms.PSet(
        nbins = cms.int32(60),
        xmin = cms.double(-3),
        xmax = cms.double(3)
      ),
      LxyPSet = cms.PSet(
        nbins = cms.int32(350),
        xmin = cms.double(0),
        xmax = cms.double(70)
      ),
      chi2oNDFPSet = cms.PSet(
        nbins = cms.int32(100),
        xmin = cms.double(0),
        xmax = cms.double(30)
      ),
      puPSet = cms.PSet(
        nbins = cms.int32(100),
        xmin = cms.double(-0.5),
        xmax = cms.double(99.5)
      ),
      lsPSet = cms.PSet(
        nbins = cms.int32(2000),
        xmin = cms.double(0),
        xmax = cms.double(2000)
      )
    ),
    genericTriggerEventPSet = cms.PSet(
      ReadPrescalesFromFile = cms.bool(False),
      andOr = cms.bool(False),
      andOrDcs = cms.bool(False),
      andOrHlt = cms.bool(False),
      andOrL1 = cms.bool(False),
      errorReplyDcs = cms.bool(False),
      errorReplyHlt = cms.bool(False),
      errorReplyL1 = cms.bool(False),
      l1BeforeMask = cms.bool(False),
      stage2 = cms.bool(False),
      dcsInputTag = cms.InputTag('scalersRawToDigi'),
      dcsRecordInputTag = cms.InputTag('onlineMetaDataDigis'),
      hltInputTag = cms.InputTag('TriggerResults', '', 'HLT'),
      l1tAlgBlkInputTag = cms.InputTag('gtStage2Digis'),
      l1tExtBlkInputTag = cms.InputTag('gtStage2Digis'),
      dbLabel = cms.string(''),
      hltDBKey = cms.string(''),
      dcsPartitions = cms.vint32(),
      hltPaths = cms.vstring(),
      l1Algorithms = cms.vstring(),
      verbosityLevel = cms.uint32(0)
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
