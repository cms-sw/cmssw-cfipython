import FWCore.ParameterSet.Config as cms

hltEgammaHLTCombinedIsolationProducer = cms.EDProducer('EgammaHLTCombinedIsolationProducer',
  recoEcalCandidateProducer = cms.InputTag('hltL1SeededRecoEcalCandidate'),
  IsolationMapTags = cms.VInputTag(),
  IsolationWeight = cms.vdouble()
)
