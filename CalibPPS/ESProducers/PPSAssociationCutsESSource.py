import FWCore.ParameterSet.Config as cms

def PPSAssociationCutsESSource(**kwargs):
  mod = cms.ESSource('PPSAssociationCutsESSource',
    ppsAssociationCutsLabel = cms.string(''),
    configuration = cms.VPSet(
    ),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
