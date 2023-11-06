import FWCore.ParameterSet.Config as cms

hgcalTestGuardRingEE = cms.EDAnalyzer('HGCalTestGuardRing',
  nameSense = cms.string('HGCalEESensitive'),
  waferFile = cms.string('testWafersEE.txt'),
  guardRingOffset = cms.double(1),
  mightGet = cms.optional.untracked.vstring
)
