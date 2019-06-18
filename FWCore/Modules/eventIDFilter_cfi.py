import FWCore.ParameterSet.Config as cms

eventIDFilter = cms.EDFilter('ModuloEventIDFilter',
  modulo = cms.required.uint32,
  offset = cms.required.uint32,
  mightGet = cms.optional.untracked.vstring
)
