import FWCore.ParameterSet.Config as cms

hltEgammaHLTPixelMatchVarProducer = cms.EDProducer('EgammaHLTPixelMatchVarProducer',
  recoEcalCandidateProducer = cms.InputTag('hltL1SeededRecoEcalCandidate'),
  pixelSeedsProducer = cms.InputTag('electronPixelSeeds'),
  dPhi1SParams = cms.PSet(),
  dPhi2SParams = cms.PSet(),
  dRZ2SParams = cms.PSet(),
  productsToWrite = cms.int32(0)
)
