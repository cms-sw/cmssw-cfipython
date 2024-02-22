import FWCore.ParameterSet.Config as cms

lhcInfoProducer = cms.EDProducer('LHCInfoProducer',
  lhcInfoLabel = cms.string(''),
  lhcInfoPerLSLabel = cms.string(''),
  lhcInfoPerFillLabel = cms.string(''),
  useNewLHCInfo = cms.bool(True),
  mightGet = cms.optional.untracked.vstring
)
