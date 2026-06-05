import FWCore.ParameterSet.Config as cms

def CandidateChargeBTagESProducer(*args, **kwargs):
  mod = cms.ESProducer('CandidateChargeBTagESProducer',
    useCondDB = cms.bool(False),
    gbrForestLabel = cms.string(''),
    weightFile = cms.FileInPath(''),
    useAdaBoost = cms.bool(True),
    jetChargeExp = cms.double(0.8),
    svChargeExp = cms.double(0.5),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
