import FWCore.ParameterSet.Config as cms

QGTagger = cms.EDProducer('QGTagger',
  systematicsLabel = cms.string(''),
  jec = cms.InputTag('')
)
