import FWCore.ParameterSet.Config as cms

patJetIDValueMapProducer = cms.EDProducer('PatJetIDValueMapProducer',
  src = cms.required.InputTag,
  filterParams = cms.PSet(
    version = cms.string('RUN3WINTER22PUPPI'),
    quality = cms.string('TIGHT'),
    cutsToIgnore = cms.optional.vstring
  ),
  mightGet = cms.optional.untracked.vstring
)
