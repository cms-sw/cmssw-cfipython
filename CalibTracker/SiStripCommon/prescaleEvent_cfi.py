import FWCore.ParameterSet.Config as cms

prescaleEvent = cms.EDFilter('PrescaleEventFilter',
  prescale = cms.uint32(1),
  offset = cms.uint32(0)
)
