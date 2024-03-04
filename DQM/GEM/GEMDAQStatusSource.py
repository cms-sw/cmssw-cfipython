import FWCore.ParameterSet.Config as cms

def GEMDAQStatusSource(**kwargs):
  mod = cms.EDProducer('GEMDAQStatusSource',
    VFATInputLabel = cms.InputTag('muonGEMDigis', 'VFATStatus'),
    OHInputLabel = cms.InputTag('muonGEMDigis', 'OHStatus'),
    AMCInputLabel = cms.InputTag('muonGEMDigis', 'AMCStatus'),
    AMC13InputLabel = cms.InputTag('muonGEMDigis', 'AMC13Status'),
    AMCSlots = cms.int32(13),
    runType = cms.untracked.string('relval'),
    logCategory = cms.untracked.string('GEMDAQStatusSource'),
    useDBEMap = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
