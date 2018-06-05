import FWCore.ParameterSet.Config as cms

HLLHCEvtVtxGenerator = cms.EDProducer('HLLHCEvtVtxGenerator',
  MeanXIncm = cms.double(0),
  MeanYIncm = cms.double(0),
  MeanZIncm = cms.double(0),
  TimeOffsetInns = cms.double(0),
  EprotonInGeV = cms.double(7000),
  CrossingAngleInurad = cms.double(510),
  CrabbingAngleCrossingInurad = cms.double(380),
  CrabbingAngleSeparationInurad = cms.double(0),
  CrabFrequencyInMHz = cms.double(400),
  RF800 = cms.bool(False),
  BetaCrossingPlaneInm = cms.double(0.2),
  BetaSeparationPlaneInm = cms.double(0.2),
  HorizontalEmittance = cms.double(2.5e-06),
  VerticalEmittance = cms.double(2.05e-06),
  BunchLengthInm = cms.double(0.09)
)
