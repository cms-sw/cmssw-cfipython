import FWCore.ParameterSet.Config as cms

demo = cms.EDProducer('DemoNormalDQMEDAnalyzer',
  folder = cms.string('MY_FOLDER'),
  mightGet = cms.optional.untracked.vstring
)
