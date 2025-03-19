import FWCore.ParameterSet.Config as cms

def ElectronEfficiencyPlotter(*args, **kwargs):
  mod = cms.EDProducer('ElectronEfficiencyPlotter',
    ptBin = cms.int32(5),
    ptMin = cms.double(0),
    ptMax = cms.double(100),
    sctElectronID = cms.string(''),
    folder = cms.string(''),
    srcFolder = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
