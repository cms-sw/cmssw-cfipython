import FWCore.ParameterSet.Config as cms

Phase1L1TJetProducer = cms.EDProducer('Phase1L1TJetProducer',
  inputCollectionTag = cms.InputTag('l1pfCandidates', 'Puppi'),
  etaBinning = cms.required.vdouble,
  nBinsPhi = cms.uint32(72),
  phiLow = cms.double(-3.1415926535897931),
  phiUp = cms.double(3.1415926535897931),
  jetIEtaSize = cms.uint32(7),
  jetIPhiSize = cms.uint32(7),
  seedPtThreshold = cms.double(5),
  puSubtraction = cms.bool(False),
  outputCollectionName = cms.string('UncalibratedPhase1L1TJetFromPfCandidates'),
  vetoZeroPt = cms.bool(True),
  mightGet = cms.optional.untracked.vstring
)
