import FWCore.ParameterSet.Config as cms

GEMDQMHarvester = cms.EDProducer('GEMDQMHarvester',
  cutErr = cms.double(0.05),
  cutLowErr = cms.double(0),
  cutWarn = cms.double(0.05),
  mightGet = cms.optional.untracked.vstring
)
