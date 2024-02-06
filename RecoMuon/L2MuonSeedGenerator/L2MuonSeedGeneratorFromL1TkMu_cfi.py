import FWCore.ParameterSet.Config as cms

L2MuonSeedGeneratorFromL1TkMu = cms.EDProducer('L2MuonSeedGeneratorFromL1TkMu',
  InputObjects = cms.InputTag('hltGmtStage2Digis'),
  Propagator = cms.string(''),
  L1MinPt = cms.double(-1),
  L1MaxEta = cms.double(5),
  SetMinPtBarrelTo = cms.double(3.5),
  SetMinPtEndcapTo = cms.double(1),
  MinPL1Tk = cms.double(3.5),
  MinPtL1TkBarrel = cms.double(3.5),
  UseOfflineSeed = cms.untracked.bool(False),
  UseUnassociatedL1 = cms.bool(True),
  MatchDR = cms.vdouble(0.3),
  EtaMatchingBins = cms.vdouble(
    0,
    2.5
  ),
  OfflineSeedLabel = cms.untracked.InputTag(''),
  ServiceParameters = cms.PSet(
    Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
    RPCLayers = cms.bool(True),
    UseMuonNavigation = cms.untracked.bool(True)
  ),
  mightGet = cms.optional.untracked.vstring
)
