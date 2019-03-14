import FWCore.ParameterSet.Config as cms

L2MuonSeedGeneratorFromL1T = cms.EDProducer('L2MuonSeedGeneratorFromL1T',
  GMTReadoutCollection = cms.InputTag(''),
  InputObjects = cms.InputTag('hltGmtStage2Digis'),
  Propagator = cms.string(''),
  L1MinPt = cms.double(-1),
  L1MaxEta = cms.double(5),
  L1MinQuality = cms.uint32(0),
  UseOfflineSeed = cms.untracked.bool(False),
  UseUnassociatedL1 = cms.bool(True),
  MatchDR = cms.vdouble(0.3),
  EtaMatchingBins = cms.vdouble(
    0,
    2.5
  ),
  CentralBxOnly = cms.bool(True),
  OfflineSeedLabel = cms.untracked.InputTag(''),
  ServiceParameters = cms.PSet(
    Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
    RPCLayers = cms.bool(True),
    UseMuonNavigation = cms.untracked.bool(True)
  )
)
