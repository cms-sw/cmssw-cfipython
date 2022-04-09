import FWCore.ParameterSet.Config as cms

gemEffByGEMCSCSegmentClient = cms.EDProducer('GEMEffByGEMCSCSegmentClient',
  folder = cms.untracked.string('GEM/Efficiency/GEMCSCSegment'),
  logCategory = cms.untracked.string('GEMEffByGEMCSCSegmentClient'),
  mightGet = cms.optional.untracked.vstring
)
