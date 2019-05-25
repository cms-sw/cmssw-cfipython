import FWCore.ParameterSet.Config as cms

hltEgammaHLTElectronCombinedIsolationProducer = cms.EDProducer('EgammaHLTElectronCombinedIsolationProducer',
  electronProducer = cms.InputTag(''),
  recoEcalCandidateProducer = cms.InputTag(''),
  CaloIsolationMapTags = cms.VInputTag(),
  TrackIsolationMapTag = cms.InputTag(''),
  CaloIsolationWeight = cms.vdouble(),
  TrackIsolationWeight = cms.double(0)
)
