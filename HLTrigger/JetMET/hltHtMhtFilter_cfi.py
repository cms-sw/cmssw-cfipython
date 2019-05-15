import FWCore.ParameterSet.Config as cms

hltHtMhtFilter = cms.EDFilter('HLTHtMhtFilter',
  saveTags = cms.bool(True),
  htLabels = cms.VInputTag('hltHtMhtProducer'),
  mhtLabels = cms.VInputTag('hltHtMhtProducer'),
  minHt = cms.vdouble(250),
  minMht = cms.vdouble(70),
  minMeff = cms.vdouble(0),
  meffSlope = cms.vdouble(1)
)
