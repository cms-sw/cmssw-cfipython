import FWCore.ParameterSet.Config as cms

gemEfficiencyAnalyzerDefault = cms.EDProducer('GEMEfficiencyAnalyzer',
  name = cms.untracked.string('GlobalMuon'),
  folder = cms.untracked.string('GEM/Efficiency/type0'),
  recHitTag = cms.InputTag('gemRecHits'),
  muonTag = cms.InputTag('muons'),
  isCosmics = cms.untracked.bool(False),
  useGlobalMuon = cms.untracked.bool(True),
  useSkipLayer = cms.bool(False),
  useOnlyME11 = cms.bool(False),
  residualRPhiCut = cms.double(2),
  usePropRErrorCut = cms.bool(False),
  propRErrorCut = cms.double(1),
  usePropPhiErrorCut = cms.bool(False),
  propPhiErrorCut = cms.double(0.01),
  ptBins = cms.untracked.vdouble(
    20,
    30,
    40,
    50,
    60,
    70,
    80,
    90,
    100,
    120
  ),
  etaNbins = cms.untracked.int32(9),
  etaLow = cms.untracked.double(1.4),
  etaUp = cms.untracked.double(2.3),
  ServiceParameters = cms.PSet(),
  mightGet = cms.optional.untracked.vstring
)
