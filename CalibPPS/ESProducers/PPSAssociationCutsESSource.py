import FWCore.ParameterSet.Config as cms

def PPSAssociationCutsESSource(*args, **kwargs):
  mod = cms.ESSource('PPSAssociationCutsESSource',
    ppsAssociationCutsLabel = cms.string(''),
    configuration = cms.VPSet(
    ),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
