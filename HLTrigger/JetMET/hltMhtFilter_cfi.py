import FWCore.ParameterSet.Config as cms

hltMhtFilter = cms.EDFilter('HLTMhtFilter',
  saveTags = cms.bool(True),
  mhtLabels = cms.VInputTag('hltMhtProducer'),
  minMht = cms.vdouble(70)
)
