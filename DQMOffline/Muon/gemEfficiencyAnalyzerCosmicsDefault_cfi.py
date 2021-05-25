import FWCore.ParameterSet.Config as cms

gemEfficiencyAnalyzerCosmicsDefault = cms.EDProducer('GEMEfficiencyAnalyzer',
  name = cms.untracked.string('GlobalMuon'),
  folder = cms.untracked.string('GEM/Efficiency/type0'),
  recHitTag = cms.InputTag('gemRecHits'),
  muonTag = cms.InputTag('muons'),
  isCosmics = cms.untracked.bool(True),
  useGlobalMuon = cms.untracked.bool(False),
  useSkipLayer = cms.bool(True),
  useOnlyME11 = cms.bool(True),
  residualRPhiCut = cms.double(5),
  usePropRErrorCut = cms.bool(True),
  propRErrorCut = cms.double(2),
  usePropPhiErrorCut = cms.bool(True),
  propPhiErrorCut = cms.double(0.01),
  ptBins = cms.untracked.vdouble(
    0,
    10,
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
