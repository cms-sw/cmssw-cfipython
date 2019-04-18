import FWCore.ParameterSet.Config as cms

otherThingProd = cms.EDProducer('OtherThingProducer',
  thingTag = cms.InputTag('Thing'),
  useRefs = cms.untracked.bool(True),
  transient = cms.untracked.bool(False)
)
