import FWCore.ParameterSet.Config as cms

ppsAssociationCutsESSource = cms.ESSource('PPSAssociationCutsESSource',
  ppsAssociationCutsLabel = cms.string(''),
  configuration = cms.VPSet(
  ),
  appendToDataLabel = cms.string('')
)
