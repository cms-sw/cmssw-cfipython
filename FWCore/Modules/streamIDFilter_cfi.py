import FWCore.ParameterSet.Config as cms

streamIDFilter = cms.EDFilter('ModuloStreamIDFilter',
  modulo = cms.required.uint32,
  offset = cms.required.uint32,
  mightGet = cms.optional.untracked.vstring
)
