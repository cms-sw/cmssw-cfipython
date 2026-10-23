import FWCore.ParameterSet.Config as cms

def SiStripRegionConnectivity(*args, **kwargs):
  mod = cms.ESProducer('SiStripRegionConnectivity',
    EtaDivisions = cms.untracked.uint32(10),
    PhiDivisions = cms.untracked.uint32(10),
    EtaMax = cms.untracked.double(2.4),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
