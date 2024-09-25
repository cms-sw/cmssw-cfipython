import FWCore.ParameterSet.Config as cms

def DQMHcalIterativePhiSymAlCaReco(*args, **kwargs):
  mod = cms.EDProducer('DQMHcalIterativePhiSymAlCaReco',
    folderName = cms.string('ALCAStreamHcalIterativePhiSym'),
    hbheInput = cms.InputTag('hbhereco'),
    hfInput = cms.InputTag('hfreco'),
    hoInput = cms.InputTag('horeco'),
    hiDistr_y_nbin = cms.untracked.int32(72),
    hiDistr_y_min = cms.untracked.double(0.5),
    hiDistr_y_max = cms.untracked.double(72.5),
    hiDistr_x_nbin = cms.untracked.int32(83),
    hiDistr_x_min = cms.untracked.double(-41.5),
    hiDistr_x_max = cms.untracked.double(41.5),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
