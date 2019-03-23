import FWCore.ParameterSet.Config as cms

pfRecoTauCorrectedInvariantMassProducer = cms.EDProducer('PFRecoTauCorrectedInvariantMassProducer',
  Prediscriminants = cms.PSet(
    leadTrack = cms.PSet(),
    decayMode = cms.PSet()
  )
)
