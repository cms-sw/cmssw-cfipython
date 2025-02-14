import FWCore.ParameterSet.Config as cms

def ConsumeWhatsIt(*args, **kwargs):
  mod = cms.ESProducer('ConsumeWhatsIt',
    esInputTag_in_produce = cms.required.ESInputTag,
    esInputTagA_in_produce = cms.required.ESInputTag,
    esInputTagB_in_produce = cms.required.ESInputTag,
    esInputTagC_in_produce = cms.required.ESInputTag,
    esInputTagD_in_produce = cms.required.ESInputTag,
    esInputTag_in_produceA = cms.required.ESInputTag,
    esInputTagA_in_produceA = cms.required.ESInputTag,
    esInputTagB_in_produceA = cms.required.ESInputTag,
    esInputTagC_in_produceA = cms.required.ESInputTag,
    esInputTagD_in_produceA = cms.required.ESInputTag,
    esInputTag_in_produceB = cms.required.ESInputTag,
    esInputTagA_in_produceB = cms.required.ESInputTag,
    esInputTagB_in_produceB = cms.required.ESInputTag,
    esInputTagC_in_produceB = cms.required.ESInputTag,
    esInputTagD_in_produceB = cms.required.ESInputTag,
    esInputTag_in_produceC = cms.required.ESInputTag,
    esInputTagA_in_produceC = cms.required.ESInputTag,
    esInputTagB_in_produceC = cms.required.ESInputTag,
    esInputTagC_in_produceC = cms.required.ESInputTag,
    esInputTagD_in_produceC = cms.required.ESInputTag,
    esInputTag_in_produceD = cms.required.ESInputTag,
    esInputTagA_in_produceD = cms.required.ESInputTag,
    esInputTagB_in_produceD = cms.required.ESInputTag,
    esInputTagC_in_produceD = cms.required.ESInputTag,
    esInputTagD_in_produceD = cms.required.ESInputTag,
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
